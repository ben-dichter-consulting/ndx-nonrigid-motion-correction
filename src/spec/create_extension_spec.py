from pynwb.spec import NamespaceBuilder, NWBGroupSpec
from export_spec import export_spec


def main():
    # the values for ns_builder are auto-generated from your cookiecutter inputs
    ns_builder = NamespaceBuilder(doc='General framework for storing nonrigid motion correction of optical imaging in '
                                      'NWB:N 2.0',
                                  name='ndx-nonrigid-motion-correction',
                                  version='0.1.0',
                                  author='Ben Dichter',
                                  contact='ben.dichter@gmail.com')

    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb for more information
    nmc = NWBGroupSpec(
        neurodata_type_def='NonrigidMotionCorrection',
        neurodata_type_inc='NWBDataInterface',
        doc='General framework for storing nonrigid motion correction of optical imaging in NWB:N 2.0',
    )

    #  I think it may make more sense to store pixel_map as an x*y*z array and convert to your form
    nmc.add_dataset(name='pixel_map',
                    dtype='int',
                    shape=((None, None), (None, None, None)),
                    dims=(('x', 'y'), ('x', 'y', 'z')),
                    doc="A mapping function of pixels onto basis variables. To be fully general, this is a sparse "
                        "matrix (AxBxC) (number of voxels in each of the spatial dimensions). In standard "
                        "blockwise motion correction, this matrix is a matrix of ones. In CNMF's patches, this matrix "
                        "is a labels each non-overlapping patch with a unique int")

    nmc.add_dataset(name='data',
                    dtype='float',
                    shape=(None, None),
                    dims=('time', 'nblocks * ndims'),
                    doc="A set of (NxM) basis variables where N is the number of blocks, M is the number of spatial "
                        "dimensions (1 to 3) each defined for a set of times T (for the number of time-steps). In "
                        "standard block-wise motion correction, N = 1, in line-by-line motion correction, N = number of"
                        " lines, in CNMF's non-rigid motion correction, N = number of patches")

    nmc.add_attribute(name='interpolation_type',
                      dtype='text',
                      doc="the relationship between expected shifts and the estimated movie value. This will frequently"
                          " be either nearest neighbor (common), 1 pixel local interpolation (most common), or some "
                          "other interpolation function (least common, such as MATLAB's 3d gridded interpolation)",
                      default_value='local_interpolation')

    nmc.add_attribute(name='spatial_dimensions',
                      dtype='int',
                      shape=((2,), (3,)),
                      dims=('x, y', 'x, y, z'),
                      doc='number of pixels in each spatial dimension')

    nmc.add_attribute(name='nblocks', dtype='int', doc='number of blocks')

    new_data_types = [nmc]

    ns_builder.include_type('TimeSeries', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
